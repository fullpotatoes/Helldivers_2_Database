from django.test.runner import DiscoverRunner
from django.db import connections
import psycopg2.extensions
from django.conf import settings

class TestRunner(DiscoverRunner):
    """
    Custom test runner that closes database connections before and after tests.
    This helps prevent the "database is being accessed by other users" error
    when recreating the test database.
    """

    def setup_databases(self, **kwargs):
        """
        Close existing connections before setting up test databases.
        """
        self._close_connections()

        # Force-terminate any remaining connections to the test database
        self._terminate_test_db_connections()

        return super().setup_databases(**kwargs)

    def teardown_databases(self, old_config, **kwargs):
        """
        Close connections before tearing down test databases.
        """
        self._close_connections()

        # Force-terminate any remaining connections to the test database
        self._terminate_test_db_connections()

        return super().teardown_databases(old_config, **kwargs)

    def _close_connections(self):
        """
        Close all Django database connections.
        """
        for conn in connections.all():
            conn.close_if_unusable_or_obsolete()
            conn.close()

    def _terminate_test_db_connections(self):
        """
        Forcefully terminate any remaining connections to the test database.
        This is a more aggressive approach to ensure no connections remain.
        """
        try:
            db_settings = settings.DATABASES['default']
            test_db_name = 'test_' + db_settings['NAME']

            # Connect to postgres database to run administrative commands
            conn = psycopg2.connect(
                dbname='postgres',
                user=db_settings['USER'],
                password=db_settings['PASSWORD'],
                host=db_settings['HOST'],
                port=db_settings['PORT']
            )
            conn.autocommit = True

            with conn.cursor() as cursor:
                # Terminate all connections to the test database
                cursor.execute(
                    "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = %s",
                    [test_db_name]
                )

            conn.close()
        except Exception as e:
            print(f"Warning: Could not terminate test database connections: {e}")
            # Continue even if this fails - it's just an extra precaution

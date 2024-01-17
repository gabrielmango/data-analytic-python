class GenerateSql:
    """Provides methods for generating SQL scripts."""

    def create_file(self, name_file: str, content: str) -> None:
        """Creates a file with the given name and content."""
        with open(name_file, 'a+') as file:
            file.write(content)

    def script_delete_sql(
        self, name: str, locate: str, uuid: str, uuid_2: bool = False
    ) -> str:
        """Generates a SQL script for deleting records based on name, location, and UUID."""
        if uuid_2:
            return f"""-- {name}
    IF EXISTS (SELECT * FROM {locate} WHERE co_uuid_2 = '{uuid}')
    THEN
        DELETE * FROM {locate} WHERE co_uuid_2 = '{uuid}';
    END IF;
    
"""
        else:
            return f"""-- {name}
    IF EXISTS (SELECT * FROM {locate} WHERE co_uuid = '{uuid}')
    THEN
        DELETE * FROM {locate} WHERE co_uuid = '{uuid}';
    END IF;

"""

    def script_base(self, components):
        """Generates a base SQL script by combining the provided components."""
        return f"""DO $$
BEGIN
{components}
END $$;
"""

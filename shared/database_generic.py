from shared.pd_exception import DatabaseException

class GenericDatabase:

    def execute(self, sql, args=None):
        raise NotImplementedError()

    def value(self, sql, args=None, default=None, fail_on_missing=False):
        try:
            return self.values(sql, args)[0]
        except IndexError as e:
            if fail_on_missing:
                raise DatabaseException('Failed to get a value from `{sql}`'.format(sql=sql)) from e
            else:
                return default

    def values(self, sql, args=None):
        rs = self.execute(sql, args)
        return [list(row.values())[0] for row in rs]

    def insert(self, sql, args=None):
        raise NotImplementedError()

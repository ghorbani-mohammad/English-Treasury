class ReadOnlyAdminDateFieldsMIXIN:
    base_readonly_fields = ("created_at", "updated_at", "deleted_at")

    def get_readonly_fields(self, request, obj=None):
        if self.readonly_fields:
            return set(self.readonly_fields + self.base_readonly_fields)
        return self.base_readonly_fields

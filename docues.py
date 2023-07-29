class PermissionClass(BasePermission):
  def has_permission(self, request, view):
    # Logic

# Implicitly defines CRUD endpoints
class UserViewSet(ReadOnlyModelViewSet):
  permission_classes = [PermissionClass]

  def get_serializer_class(self):
  # Logic

  def get_queryset(self):
  # Logic
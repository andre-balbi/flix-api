from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET", "OPTIONS", "HEAD"]:  # Métodos safes
            # A sintaxe padrao para verificar permissões é a seguinte:
            #   request.user.has_permission('<app_name>.<permission_name>')
            # Onde:
            #   - <app_name>   o nome do app que contém a permissão
            #   - <permission_name>   o nome da permissão (painel de admin do Django)
            return request.user.has_perm("genres.view_genre")

        if request.method == "POST":
            return request.user.has_perm("genres.add_genre")

        if request.method in ["PUT", "PATCH"]:
            return request.user.has_perm("genres.change_genre")

        if request.method == "DELETE":
            return request.user.has_perm("genres.delete_genre")

        return False

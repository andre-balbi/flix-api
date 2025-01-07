from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    # Verifica se o usuario tem permissao para realizar a acao
    def has_permission(self, request, view):
        # Recupera a permissao dinamicamente com base no metodo da requisicao e na view
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method, view=view
        )
        # Se a permissao nao for encontrada, retorna False
        if not model_permission_codename:
            return False
        # Verifica se o usuario tem a permissao
        return request.user.has_perm(model_permission_codename)

    # Recupera a permissao dinamicamente com base no modelo da view
    def __get_model_permission_codename(self, method, view):
        try:
            # Recupera o nome do modelo
            model_name = view.queryset.model._meta.model_name
            # Recupera o nome do app do modelo
            app_label = view.queryset.model._meta.app_label
            # Recupera a acao com base no metodo da requisicao
            action = self.__get_action_sufix(method=method)
            # Monta a permissao dinamicamente
            return f"{app_label}.{action}_{model_name}"
        except AttributeError:
            # Se a permissao nao for encontrada, retorna None
            return None

    # Recupera a acao com base no metodo da requisicao
    def __get_action_sufix(self, method):
        # Dicionario com as acoes e seus respectivos metodos
        method_actions = {
            "GET": "view",
            "POST": "add",
            "PUT": "change",
            "PATCH": "change",
            "DELETE": "delete",
            "HEAD": "view",
            "OPTIONS": "view",
        }
        # Retorna a acao com base no metodo da requisicao ("" caso nao seja encontrada)
        return method_actions.get(method, "")

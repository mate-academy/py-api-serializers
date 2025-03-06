# this executed when we run `python manage.py test`
import sys
from rest_framework.test import APIClient as OriginalAPIClient

if "test" in sys.argv:
    class PatchedAPIClient(OriginalAPIClient):

        def get(self, path, data=None, follow=False, **extra):
            extra.setdefault("format", "json")
            return super().get(path, data, follow, **extra)

        def put(
            self,
            path,
            data=None,
            format="json",  # noqa: VNE003
            content_type=None,
            follow=False,
            **extra
        ):
            return super().put(path, data, format, content_type, follow,
                               **extra)

        def post(
            self,
            path,
            data=None,
            format="json",  # noqa: VNE003
            content_type=None,
            follow=False,
            **extra
        ):
            return super().post(path, data, format, content_type, follow,
                                **extra)

        def patch(
            self,
            path,
            data=None,
            format="json",  # noqa: VNE003
            content_type=None,
            follow=False,
            **extra
        ):
            return super().patch(path, data, format, content_type, follow,
                                 **extra)

        def delete(
            self,
            path,
            data=None,
            format="json",  # noqa: VNE003
            content_type=None,
            follow=False,
            **extra
        ):
            return super().delete(
                path, data, format, content_type, follow, **extra
            )


    # monkeypatching the original APIClient class
    sys.modules["rest_framework.test"].APIClient = PatchedAPIClient

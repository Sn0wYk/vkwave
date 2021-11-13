from vkwave.types.responses import *
from ._category import Category
from ._utils import get_params


class Search(Category):
    async def get_hints(
        self,
        return_raw_response: bool = False,
        q: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        filters: Optional[List[str]] = None,
        fields: Optional[List[str]] = None,
        search_global: Optional[bool] = None,
    ) -> Union[dict, SearchGetHintsResponse]:
        """
        :param q: - Search query string.
        :param offset: - Offset for querying specific result subset
        :param limit: - Maximum number of results to return.
        :param filters:
        :param fields:
        :param search_global:
        :param return_raw_response: - return result at dict
        :return:
        """

        params = get_params(locals())

        raw_result = await self.api_request("getHints", params)
        if return_raw_response:
            return raw_result

        result = SearchGetHintsResponse(**raw_result)
        return result

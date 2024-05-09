import asyncio
import httpx
from parsel import Selector


class HouseCrawler:
    MAIN_URL = "https://www.house.kg/kupit-dom?region=all&sort_by=upped_at+desc"
    BASE_URL = "https://www.house.kg"

    async def get_page(self, url: str, client: httpx.AsyncClient):
        response = await client.get(url)
        self.page = response.text


    def get_house_links(self, page: str):
        html = Selector(self.page)
        link = html.css(".listings-wrapper a::attr(href)").getall()
        full_links = list(map(lambda x: self.BASE_URL + x, link))
        return full_links


    async def get_house(self):
        tasks = []
        async with httpx.AsyncClient() as client:
            for i in range(1,6):
                url = f"{self.MAIN_URL}&page={i}"
                task = asyncio.create_task(self.get_page(url, client))
                tasks.append(task)

            results = await asyncio.gather(*tasks)
            all_links = []
            for result in results:
                links = self.get_house_links(result)
                all_links.extend(links)

        return all_links

if __name__ == "__main__":
    crawler = HouseCrawler()
    asyncio.run(crawler.get_house())
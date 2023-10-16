import trio
from maltego_trx.maltego import MaltegoTransform, MaltegoMsg
from maltego_trx.transform import DiscoverableTransform
from extensions import registry, sumoMaltego_set
import sumoSearch

@registry.register_transform(
    display_name="Retreive escort ads", 
    input_entity="maltego.PhoneNumber",
    description='Retrieves escort ads from sumosearc.ch using phone number',
    settings=[],
    output_entities=["maltego.URL"],
    transform_set=sumoMaltego_set
    )
class phoneToAds(DiscoverableTransform):
    
    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):

        async def main():

            # Retrieve name from entity
            phone_number = request.Value

            # Query SumoSear.ch
            wrestler = sumoSearch.sumo()
            results = wrestler.phone_lookup(phone_number)

            # Convert records to entities
            for result in results:
                parts = result.split('/')

                url = response.addEntity("maltego.URL")
                url.addProperty("url", value = result)
                url.addProperty("short-title", value = parts[-1])
                url.addProperty("title", value = '/'.join(parts[-2:]))

        trio.run(main) # running our async code in a non-async code
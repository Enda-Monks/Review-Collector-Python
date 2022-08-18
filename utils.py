import time
import random
from datetime import datetime
# import elasticsearch
# from elasticbud import (
#     get_elasticsearch_client,
#     index_to_elasticsearch
# )

def random_sleep(min_time: float) -> None: # Tasker's func - https://github.com/z-tasker/qloader/blob/master/qloader/browserdriver.py
    """
        Fuzz wait times between [min_time, min_time*2]
    """
    time.sleep(min_time + min_time * random.random())

def stringToDate(dateStr: str, dateFormat) -> datetime:
    return datetime.strptime(dateStr, dateFormat)


# @pytest.mark.depends(on=["test_check_elasticsearch"]) # Tasker's func https://github.com/z-tasker/elasticbud/blob/bd539e2df4671a762b0f8fd7dce2d922e990174b/tests/test_integration_flow.py#L53
# def test_index_to_elasticsearch() -> None:
#     client = get_elasticsearch_client()

#     docs = json.loads(
#         Path(__file__).parent.joinpath(f"{TEST_INDEX_NAME}.json").read_text()
#     )

#     if client.indices.exists(index=TEST_INDEX_NAME):
#         client.indices.delete(index=TEST_INDEX_NAME)

#     index_template = json.loads(
#         Path(__file__).parent.joinpath(f"{TEST_INDEX_NAME}.template.json").read_text()
#     )

#     # fresh naive indexing operation
#     index_to_elasticsearch(
#         elasticsearch_client=client,
#         index=TEST_INDEX_NAME,
#         index_template=index_template,
#         docs=docs[:500],  # first 500 docs in
#     )

#     # dirty indexing operation with idempotency
#     index_to_elasticsearch(
#         elasticsearch_client=client,
#         index=TEST_INDEX_NAME,
#         docs=docs[300:],  # from the 300th document onward (200 already exist)
#         identity_fields=["date", "article"],
#         batch_size=300,  # test batch size customization
#     )

#     client.indices.refresh(index=TEST_INDEX_NAME)

#     assert int(
#         client.cat.count(TEST_INDEX_NAME, params={"format": "json"})[0]["count"]
#     ) == len(docs)

#     applied_mapping = client.indices.get_mapping(TEST_INDEX_NAME)
#     source_mapping = {TEST_INDEX_NAME: {"mappings": index_template["mappings"]}}

#     assert applied_mapping == source_mapping


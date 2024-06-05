import pytest
from strawberry_django.test.client import TestClient


@pytest.fixture()
def api_client() -> TestClient:
    return TestClient("/graphql")


def test_schema(api_client):
    query = """
    query ColorWithFruits {
      colors(first: 1) {
        totalCount
        edges {
          node {
            id
            fruits(filters: {name: {startsWith: "Straw"}}) {
              edges {
                node {
                  id
                  name
                }
              }
            }
          }
        }
      }
      fruits(filters: {name: {startsWith: "Straw"}}) {
        totalCount
      }
    }
    """
    result = api_client.query(query=query)
    assert result.data == {}

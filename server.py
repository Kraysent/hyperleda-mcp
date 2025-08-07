from hyperleda import data
import fastmcp

mcp = fastmcp.FastMCP(
    "HyperLEDA",
    instructions="""
    This server provides functionality to work with extragalactic objects.
""",
)


@mcp.tool(tags=["objects"])
async def get_object_by_id(pgc: int) -> str:
    """Get extragalactic object details by PGC number.

    Args:
        pgc: PGC number of the object.
    """

    client = data.HyperLedaDataClient()
    resp = client.query_simple(data.QuerySimpleRequestSchema(pgcs=[pgc]))

    return resp.model_dump_json()


@mcp.tool()
async def get_objects(ra: float, dec: float, radius: float) -> str:
    """Search for extragalactic objects within a circular region.

    Args:
        ra: Right ascension in degrees (0-360)
        dec: Declination in degrees (-90 to +90)
        radius: Search radius in degrees
    """

    client = data.HyperLedaDataClient()
    resp = client.query_simple(
        data.QuerySimpleRequestSchema(ra=ra, dec=dec, radius=radius)
    )

    return resp.model_dump_json()


if __name__ == "__main__":
    print("Starting `hyperleda` MCP server")
    mcp.run(transport="sse")

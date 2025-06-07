from hyperleda import data
import hyperleda
from mcp.server import fastmcp

mcp = fastmcp.FastMCP("hyperleda")


@mcp.tool()
async def get_objects_num(ra: float, dec: float, radius: float) -> int | str:
    """Returns a number of galactic objects inside a given radius
    around given coordinates. If there was an error, it will return a string containing the description of the error.

    Args:
        ra: J2000 right ascension of the position in degrees.
        dec: J2000 declination of the position in degrees.
        radius: Radius, in which objects will be counted, in degrees.
    """

    client = data.HyperLedaDataClient(hyperleda.PROD_ENDPOINT)
    try:
        d = client.query_simple(
            data.QuerySimpleRequestSchema(ra=ra, dec=dec, radius=radius, page_size=25)
        )
    except Exception as e:
        print(str(e))
        return str(e)

    return len(d.objects)


if __name__ == "__main__":
    print("Starting `hyperleda` MCP server")
    mcp.run(transport="sse")

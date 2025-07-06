# main.py
from mcp.server.fastmcp import FastMCP
import tools

mcp = FastMCP("host info mcp")
mcp.add_tool(tools.get_host_info)

@mcp.tool()
def foo():
    return ""

def main():
    mcp.run("stdio") # 也可以以 sse 方式运行，使用 http 方式运行


if __name__ == "__main__":
    main()

    

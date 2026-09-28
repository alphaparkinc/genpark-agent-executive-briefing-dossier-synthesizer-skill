import sys
import json
from client import ExecutiveBriefingSynthesizer

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "synthesize_executive_brief",
                        "description": "Synthesizes multi-channel workplace updates into a structured executive morning brief.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "department": {"type": "string"},
                                "timeframe_hours": {"type": "integer"}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        args = params.get("arguments", {})
        synth = ExecutiveBriefingSynthesizer()
        res = synth.synthesize(args.get("department", "PRODUCT_AND_ENGINEERING"), args.get("timeframe_hours", 24))
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    synth = ExecutiveBriefingSynthesizer()
    print(json.dumps(synth.synthesize(), indent=2))

if __name__ == "__main__":
    main()

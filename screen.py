class Screen:
    def draw(text):
        box = {
            "nw": "╔",
            "h": "═",
            "ne": "╗",
            "v": "║",
            "se": "╝",
            "sw": "╚",
        }

        lines = text.splitlines()
        width = max(len(s) for s in lines)
        res = [box["nw"] + box["h"] * width + box["ne"]]
        for s in lines:
            res.append(box["v"] + (s + " " *width)[:width] + box["v"])
        res.append(box["sw"] + box["h"] * width + box["se"])
        return "\n".join(res)
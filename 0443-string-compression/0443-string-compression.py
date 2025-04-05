class Solution:
    def compress(self, chars: List[str]) -> int:
        
        write = 0  # Index to write the compressed string
        read = 0   # Index to read through the original string

        while read < len(chars):
            char = chars[read]
            count = 0

            
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            
            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
    # def compress(self, chars: List[str]) -> int:
    #     if len(chars) == 1:
    #         return 1

    #     res = []
    #     graph = {}
    #     prev = chars[0]
    #     count = 1

    #     for i in range(1, len(chars)):
    #         if chars[i] == prev:
    #             count += 1
    #         else:
    #             graph[prev] = count
    #             prev = chars[i]
    #             count = 1
    #     graph[prev] = count  # Add the last group

    #     # Rebuild compressed list
    #     for key, val in graph.items():
    #         res.append(key)
    #         if val > 1:
    #             for digit in str(val):
    #                 res.append(digit)

    #     # Update original list in-place
    #     for i in range(len(res)):
    #         chars[i] = res[i]

    #     return len(res)

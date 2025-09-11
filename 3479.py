class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        sect_mx = []
        m = len(baskets)
        a = int(math.sqrt(m))

        cnt = 0
        mx = 0
        for i in range(m):
            if cnt == a:
                sect_mx.append(mx)
                mx = baskets[i]
                cnt = 1
            else:
                cnt += 1
                mx = max(mx, baskets[i])

        sect_mx.append(mx)

        remain = 0

        for fruit in fruits:
            k = 0
            set_flag = 1

            for j in range(0, m, a):
                if sect_mx[k] < fruit:
                    k += 1
                    continue

                for r in range(j, min(j + a, m)):
                    if baskets[r] >= fruit:
                        set_flag = 0
                        baskets[r] = 0
                        break

                if set_flag == 0:
                    sect_mx[k] = 0
                    for r in range(j, min(j + a, m)):
                        sect_mx[k] = max(baskets[r], sect_mx[k])
                    break

                k += 1

            remain += set_flag

        return remain
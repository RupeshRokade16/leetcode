class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Realized I had to do a nested binary search
        For the outer one, I am using lower and higher of the middle array
        to determine how I move next
        """
        
        L, R = 0, len(matrix) - 1
        #first find correct matrix with binary search
        while L <= R:
            mid = (L + R)//2
            #print("Search space", matrix[mid])
            
            lower, higher = matrix[mid][0], matrix[mid][-1]
            #print("Search space lower higher", matrix[mid][0], matrix[mid][-1])
            #return True

            if target < lower:
                R = mid - 1
                continue

            if target > higher:
                L = mid + 1   
                continue

            if target >= lower and target <= higher:
                if target == lower or target==higher:
                    return True
                #Binary search
                #Valid search space and return answer
                #print("Entered search space", arr, target)
                arr = matrix[mid]
                l, r = 0, len(arr) - 1
                print(arr, l, r)
                #return True

                while l <= r:
                    m = (l+r)//2
                    if arr[m] < target:
                        l = m + 1
                        continue
                    if arr[m] > target:
                        r = m - 1
                        continue
                    elif arr[m] == target:
                        return True
                return False
        return False
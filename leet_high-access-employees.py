class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        dict = {}
        for item in access_times:
            key = item[0]
            value = item[1]
            
            if key not in dict:
                dict[key] = []
            dict[key].append(value)
            
        sorted_result = {key: sorted(values) for key, values in dict.items()}  
        result_list = []
        for key,values in sorted_result.items():
            if len(values) > 2:
                for i in range(len(values) -2):
                    if int(values[i+2]) - int(values[i]) <= 99 and len(values) > 2 and key not in result_list:

                        result_list.append(key)
            else:
                continue
        return(result_list)
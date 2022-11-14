class Solution:
    def numberToWords(self, num: int) -> str:
        def ones(num):
            hashmap = {
                1 : "One",
                2 : "Two",
                3 : "Three",
                4 : "Four",
                5 : "Five",
                6 : "Six",
                7 : "Seven",
                8 : "Eight",
                9 : "Nine"
            }
            return hashmap[num]
        
        def tenToNineteen(num):
            hashmap = {
                10 : "Ten",
                11 : "Eleven",
                12 : "Twelve",
                13 : "Thirteen",
                14 : "Fourteen",
                15 : "Fifteen",
                16 : "Sixteen",
                17 : "Seventeen",
                18 : "Eighteen",
                19 : "Nineteen"
            }
            return hashmap[num]
        
        def tens(num):
            hashmap = {
                2 : "Twenty",
                3 : "Thirty",
                4 : "Forty",
                5 : "Fifty",
                6 : "Sixty",
                7 : "Seventy",
                8 : "Eighty",
                9 : "Ninety"
            }
            return hashmap[num]
        
        def parse(num):
            string = ""
            if num >= 100:
                string += ones(num//100) + " Hundred"
                num = num%100
            if num >= 20:
                if len(string) > 0:
                    string += " "
                print(num//10)
                string += tens(num//10)
                num = num%10
            if num <= 19 and num >= 10:
                if len(string) > 0:
                    string += " "
                string += tenToNineteen(num)
                return string
            if num < 10 and num > 0:
                if len(string) > 0:
                    string += " "
                string += ones(num)
                return string
            if num == 0: #maybe num%100 or num%10 == 0
                return string
        
        """
        def parse(num, output):
            if num >= 100:
                output += ones(num//100) + " Hundred"
                num = num%100
            if num >= 20:
                if len(output) > 0:
                    output += " "
                output += tens(num//10)
                num = num%10
            if num <= 19 and num >= 10:
                if len(output) > 0:
                    output += " "
                output += tenToNineteen(num)
                return output
            if num < 10:
                if len(output) > 0:
                    output += " "
                output += ones(num)
                return output
        """    
        output = ""
        
        #check how large the number is
        #if any of these values are non-zero, that means that the number is larger than it, and appropriate word needs to be added
        billion = num//1000000000
        million = (num - billion * 1000000000)//1000000
        thousand = (num - billion * 1000000000 - million * 1000000)//1000
        rest = (num - billion * 1000000000 - million * 1000000 - thousand * 1000)
        
        if not num or num == 0:
            return "Zero"
        print(billion)
        print(million)
        print(thousand)
        print(rest)
        #add large suffixes
        if billion:
            output += parse(billion) + " Billion"
        print(output)
        if million:
            if len(output) > 0:
                output += " "
            output += parse(million) + " Million"
        print(output)
        if thousand:
            if len(output) > 0:
                output += " "
            output += parse (thousand) + " Thousand"
        if rest:
            if len(output) > 0:
                output += " "
            output += parse(rest)
        return output

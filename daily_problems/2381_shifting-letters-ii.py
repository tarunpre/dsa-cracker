class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        # initiate empty array
        darray = [0] * len(s)
        for k in shifts:
            fr = k[0]
            to = k[1]
            dr = k[2]
            if dr == 1:
                darray[fr] += 1
                if to + 1 < len(darray):
                    darray[to+1]  -= 1
            else:
                darray[fr] -= 1
                if to + 1 < len(darray):
                    darray[to+1] += 1
        result = list(s)
        number_of_shifts = 0

        # Apply the shifts to the string
        for i in range(len(s)):
            number_of_shifts = (
                number_of_shifts + darray[i]
            ) % 26  # Update cumulative shifts, keeping within the alphabet range
            if number_of_shifts < 0:
                number_of_shifts += 26  # Ensure non-negative shifts

            # Calculate the new character by shifting `s[i]`
            shifted_char = chr(
                (ord(s[i]) - ord("a") + number_of_shifts) % 26 + ord("a")
            )
            result[i] = shifted_char

        return "".join(result)
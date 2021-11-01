# Add two binary numbers given to you as strings of "0"s and "1"s.
# The result should be the string of "0"s and "1"s representing the numbers' sum.

# "11" + "101" -> "1000"

# "93" + "149" -> "242"


#  ``
#  111
#  111
# -----
# 1110

# div_mod(n, k) = (n/k, n%k)

# int(a[i]) + int(b[j])


def add_binary(a: str, b: str) -> str:
	# string 1:  10   111  111
	# string 2: 101   100  111
	# result:   111  1011 1110
	len1 = len(a)
	len2 = len(b)
	# what if len1 != len2. zfill is handy
	max_len = max(len1, len2)
	str1 = a.zfill(max_len)
	str2 = b.zfill(max_len)
	i = max_len - 1
	result = "" # as string
	carry = 0
	while (i >= 0):
		total = carry
		total += int(str1[i]) + int(str2[i])
		# 1 + 1 = 10 (binary) 2 in int
		# 1 + 0 or 0 + 1 = 1
		# 0 + 0 = 0
		digit = "1" if total % 2 == 1 else "0"
		result = digit + result
		if total == 2:
			carry = 1  # (binary)
		i -= 1

	# check extra final carry --> new digit
	if carry > 0:
		result = "1" + result
	return result

print(add_binary("11", "101"))
print(add_binary("111", "111"))
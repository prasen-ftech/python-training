def is_valid_expression(x):
	braces = {')':'(',']':'[','}':'{'}
	bracesStack = []
	for c in x:
		if c in braces.values():
			# print "Append to Stack"
			# print "%s in %s" %(c, bracesStack)
			bracesStack.append(c)
			# print bracesStack
		elif c in braces.keys() and len(bracesStack) > 0 and bracesStack[-1] == braces[c]:
			# print "Pop from Stack"
			# print "%s from %s" %(c, bracesStack)
			bracesStack.pop()
			# print bracesStack
		elif not c in braces.keys()+braces.values():
			continue
		else:
			return False
	if len(bracesStack) > 0:
		return False
	else:
		return True

if __name__ == "__main__":
	str = raw_input("Please Enter an Expression to Validate: ");
	if is_valid_expression(str):
		print "Its valid Expression!!"
	else:
		print "It's Invalid Expression!!"
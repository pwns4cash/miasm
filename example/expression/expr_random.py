import string

from miasm2.expression.expression_helper import ExprRandom

print "Simple expression generator\n"

depth = 8
print "- An ID:"
print ExprRandom.identifier()
print "- A number:"
print ExprRandom.number()

print "- 3 expressions (without cleaning expression cache):"
for i in xrange(3):
    print "\t%s\n" % ExprRandom.get(depth=depth, clean=False)

class ExprRandom_NoPerfect_NoReuse_UppercaseIdent(ExprRandom):
    """ExprRandom extension with:
     - perfect tree disabled
     - element reuse disabled
     - identifiers uppercased
     """

    perfect_tree = False
    reuse_element = False
    identifier_charset = string.uppercase

print "- 3 expressions with a custom generator:"
for i in xrange(3):
    print "\t%s\n" % ExprRandom_NoPerfect_NoReuse_UppercaseIdent.get(depth=depth)

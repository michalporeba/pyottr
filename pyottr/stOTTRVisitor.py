from .grammar.stOTTRParser import stOTTRParser
from .grammar.stOTTRVisitor import stOTTRVisitor as BaseVisitor
from .model import Template

class stOTTRVisitor(BaseVisitor):
    def __init__(self):
        self.templates = {}
    
    def aggregateResult(self, aggregate, nextResult):
        # This method is called by visitChildren to combine results

        # If this is the first child, return its result
        if aggregate is None:
            return nextResult

        # If this is not the first child, combine its result with the previous ones
        # Here we're just making a list of results, but you can do anything you want
        if isinstance(aggregate, list):
            return aggregate + [nextResult]
        else:
            return [aggregate, nextResult]

    def visitStOTTRDoc(self, ctx:stOTTRParser.StOTTRDocContext):
        result = self.visitChildren(ctx)
        print ("Result: ")
        print(result)
        print("-----")
        return { 'templates': self.templates }

    def visitStatement(self, ctx):
        print(f"Visited statement: {ctx.getText()}")
        return super().visitStatement(ctx)

    def visitSignature(self, ctx:stOTTRParser.SignatureContext):
        print(f"Visited signature: {ctx.getText()}")
        result = self.visitChildren(ctx)
        print(f'RESULT SIG: {result}')
        return result

    def visitTemplateName(self, ctx:stOTTRParser.TemplateNameContext):
        print(f"Visited template name: {ctx.getText()}")
        self.templates[ctx.getText()] = Template(ctx.getText())
        result = self.visitChildren(ctx)
        print(f"RESULT: {result}")
        return result
    

    # Visit a parse tree produced by stOTTRParser#parameterList.
    def visitParameterList(self, ctx:stOTTRParser.ParameterListContext):
        print(f"Visited parameter list: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#parameter.
    def visitParameter(self, ctx:stOTTRParser.ParameterContext):
        print(f"Visited parameter: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#defaultValue.
    def visitDefaultValue(self, ctx:stOTTRParser.DefaultValueContext):
        print(f"Visited default value: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#annotationList.
    def visitAnnotationList(self, ctx:stOTTRParser.AnnotationListContext):
        print(f"Visited annotation list: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#annotation.
    def visitAnnotation(self, ctx:stOTTRParser.AnnotationContext):
        print(f"Visited annotation: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#baseTemplate.
    def visitBaseTemplate(self, ctx:stOTTRParser.BaseTemplateContext):
        print(f"Visited base template : {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#template.
    def visitTemplate(self, ctx:stOTTRParser.TemplateContext):
        print(f"Visited template: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#patternList.
    def visitPatternList(self, ctx:stOTTRParser.PatternListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#instance.
    def visitInstance(self, ctx:stOTTRParser.InstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#argumentList.
    def visitArgumentList(self, ctx:stOTTRParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#argument.
    def visitArgument(self, ctx:stOTTRParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#type.
    def visitType(self, ctx:stOTTRParser.TypeContext):
        print(f"Visited type: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#listType.
    def visitListType(self, ctx:stOTTRParser.ListTypeContext):
        print(f"Visited list type: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#neListType.
    def visitNeListType(self, ctx:stOTTRParser.NeListTypeContext):
        print(f"Visited NeListType: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#lubType.
    def visitLubType(self, ctx:stOTTRParser.LubTypeContext):
        print(f"Visited LubType: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#basicType.
    def visitBasicType(self, ctx:stOTTRParser.BasicTypeContext):
        print(f"Visited basic type: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#term.
    def visitTerm(self, ctx:stOTTRParser.TermContext):
        print(f"Visited term {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#constantTerm.
    def visitConstantTerm(self, ctx:stOTTRParser.ConstantTermContext):
        print(f"Visited constant term: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#constant.
    def visitConstant(self, ctx:stOTTRParser.ConstantContext):
        print(f"Visited constant: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#none.
    def visitNone(self, ctx:stOTTRParser.NoneContext):
        print(f"Visited none: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#termList.
    def visitTermList(self, ctx:stOTTRParser.TermListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#constantList.
    def visitConstantList(self, ctx:stOTTRParser.ConstantListContext):
        print(f"Visited constant list: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#turtleDoc.
    def visitTurtleDoc(self, ctx:stOTTRParser.TurtleDocContext):
        print(f"Visited turtle doc: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#directive.
    def visitDirective(self, ctx:stOTTRParser.DirectiveContext):
        print(f"Visited directive: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#prefixID.
    def visitPrefixID(self, ctx:stOTTRParser.PrefixIDContext):
        print(f"Visited prefix ID: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#base.
    def visitBase(self, ctx:stOTTRParser.BaseContext):
        print(f"Visited base: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#sparqlBase.
    def visitSparqlBase(self, ctx:stOTTRParser.SparqlBaseContext):
        print(f"Visited SPARQL base: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#sparqlPrefix.
    def visitSparqlPrefix(self, ctx:stOTTRParser.SparqlPrefixContext):
        print(f"Visited SPARQL prefix: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#literal.
    def visitLiteral(self, ctx:stOTTRParser.LiteralContext):
        print(f"Visited literal: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#numericLiteral.
    def visitNumericLiteral(self, ctx:stOTTRParser.NumericLiteralContext):
        print(f"Visited numeric literal: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#rdfLiteral.
    def visitRdfLiteral(self, ctx:stOTTRParser.RdfLiteralContext):
        print(f"Visited rdf literal: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#iri.
    def visitIri(self, ctx:stOTTRParser.IriContext):
        print(f"Visited iri: {ctx.getText()}")
        # this would be a good place to expand iri if this is required
        return ctx.getText()


    # Visit a parse tree produced by stOTTRParser#prefixedName.
    def visitPrefixedName(self, ctx:stOTTRParser.PrefixedNameContext):
        print(f"Visited prefixed name: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#blankNode.
    def visitBlankNode(self, ctx:stOTTRParser.BlankNodeContext):
        print(f"Visited blank node: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#anon.
    def visitAnon(self, ctx:stOTTRParser.AnonContext):
        print(f"Visited anon: {ctx.getText()}")
        return self.visitChildren(ctx)

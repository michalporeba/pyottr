from .grammar.stOTTRParser import stOTTRParser
from .grammar.stOTTRVisitor import stOTTRVisitor as BaseVisitor
from .model import Parameter, Prefix, Template

class stOTTRVisitor(BaseVisitor):
    def __init__(self):
        self.templates = {}
    

    def aggregateResult(self, aggregate, nextResult):
        # This method is called by visitChildren to combine results
        if nextResult is None:
            return aggregate
        
        if aggregate is None:
            return nextResult

        if isinstance(aggregate, list):
            return aggregate + [nextResult]
        
        return [aggregate, nextResult]


    def visitStOTTRDoc(self, ctx:stOTTRParser.StOTTRDocContext):
        data = { 'prefixes': [], 'templates': [], 'other': [] }
        for c in ctx.children:
            node = self.visit(c)
            if isinstance(node, Template):
                data['templates'] += [node]
                continue
            if isinstance(node, Prefix):
                data['prefixes'] += [node]
                continue

            print(f'  statement type: {type(node)}')
            data['other'] += [node]

        return data


    def visitStatement(self, ctx):
        print(f"Visited statement: {ctx.getText()}")
        result = self.visitChildren(ctx)
        return result


    def visitSignature(self, ctx:stOTTRParser.SignatureContext):
        print(f"Visited signature: {ctx.getText()}")
        template = Template()
        for c in ctx.children:
            if isinstance(c, stOTTRParser.TemplateNameContext):
                template.iri =  self.visit(c)
                continue
            if isinstance(c, stOTTRParser.ParameterListContext):
                template.parameters = self.visit(c)

            node = self.visit(c)
            print(f' c({type(c)}), node({type(node)}) = {node}')
            
        return template


    def visitTemplateName(self, ctx:stOTTRParser.TemplateNameContext):
        return self.visitChildren(ctx)
        

    # Visit a parse tree produced by stOTTRParser#parameterList.
    def visitParameterList(self, ctx:stOTTRParser.ParameterListContext):
        print(f"Visited parameter list: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#parameter.
    def visitParameter(self, ctx:stOTTRParser.ParameterContext):
        print(f"Visited parameter: {ctx.getText()}")
        print(f' variable = {ctx.Variable()}')
        print(f' parameter mode = {"".join([str(p) for p in ctx.ParameterMode()])}')
        print(f' type = {ctx.type_()}')
        print(f' default = {ctx.defaultValue()}')
        p = Parameter(ctx.Variable())
        p.variable = ctx.Variable()
        p.defaultValue = ctx.defaultValue()
        return p


    # Visit a parse tree produced by stOTTRParser#defaultValue.
    def visitDefaultValue(self, ctx:stOTTRParser.DefaultValueContext):
        #print(f"Visited default value: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#annotationList.
    def visitAnnotationList(self, ctx:stOTTRParser.AnnotationListContext):
        #print(f"Visited annotation list: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#annotation.
    def visitAnnotation(self, ctx:stOTTRParser.AnnotationContext):
        #print(f"Visited annotation: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#baseTemplate.
    def visitBaseTemplate(self, ctx:stOTTRParser.BaseTemplateContext):
        #print(f"Visited base template : {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#template.
    def visitTemplate(self, ctx:stOTTRParser.TemplateContext):
        #print(f"Visited template: {ctx.getText()}")
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


    def visitDirective(self, ctx:stOTTRParser.DirectiveContext):
        return self.visitChildren(ctx)


    def visitPrefixID(self, ctx:stOTTRParser.PrefixIDContext):
        return Prefix(ctx.PNAME_NS(), ctx.IRIREF())


    # Visit a parse tree produced by stOTTRParser#base.
    def visitBase(self, ctx:stOTTRParser.BaseContext):
        print(f"Visited base: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#sparqlBase.
    def visitSparqlBase(self, ctx:stOTTRParser.SparqlBaseContext):
        print(f"Visited SPARQL base: {ctx.getText()}")
        return self.visitChildren(ctx)


    def visitSparqlPrefix(self, ctx:stOTTRParser.SparqlPrefixContext):
        return Prefix(ctx.PNAME_NS(), ctx.IRIREF())


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

from diogi.functions import always_a_list

from .grammar.stOTTRParser import stOTTRParser
from .grammar.stOTTRVisitor import stOTTRVisitor as BaseVisitor
from .model import (
    Basic,
    Instance,
    Iri,
    Parameter,
    Patterns,
    Prefix,
    Template,
    Type,
    TypedList,
)


class stOTTRVisitor(BaseVisitor):
    def __init__(self):
        pass

    def aggregateResult(self, aggregate, nextResult):
        if nextResult is None:
            return aggregate

        if aggregate is None:
            return nextResult

        if isinstance(aggregate, list):
            return aggregate + [nextResult]

        return [aggregate, nextResult]

    def visitStOTTRDoc(self, ctx: stOTTRParser.StOTTRDocContext):
        for c in ctx.children:
            for node in always_a_list(self.visit(c)):
                if node is not None:
                    yield node

    def visitStatement(self, ctx):
        print(f"Visited statement: {ctx.getText()}")
        return self.visitChildren(ctx)

    def visitSignature(self, ctx: stOTTRParser.SignatureContext):
        print(f"Visited signature: {ctx.getText()}")
        template = None
        for c in ctx.children:
            if isinstance(c, stOTTRParser.TemplateNameContext):
                template = Template(self.visit(c))
                continue
            if isinstance(c, stOTTRParser.ParameterListContext):
                template.add_parameters(self.visit(c))
                continue
            if isinstance(c, stOTTRParser.PatternListContext):
                pass

        return template

    def visitTemplateName(self, ctx: stOTTRParser.TemplateNameContext):
        return self.visitChildren(ctx)

    def visitParameterList(self, ctx: stOTTRParser.ParameterListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#parameter.
    def visitParameter(self, ctx: stOTTRParser.ParameterContext):
        p = Parameter(str(ctx.Variable()))
        modifiers = [str(x) for x in ctx.ParameterMode()]
        p.optional = "?" in modifiers
        p.nonblank = "!" in modifiers
        children = self.visitChildren(ctx)
        for c in always_a_list(children):
            if isinstance(c, Type):
                p.type_ = c
                continue
            p.default_value = c

        return p

    # Visit a parse tree produced by stOTTRParser#defaultValue.
    def visitDefaultValue(self, ctx: stOTTRParser.DefaultValueContext):
        # print(f"Visited default value: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#annotationList.
    def visitAnnotationList(self, ctx: stOTTRParser.AnnotationListContext):
        print(f"Visited annotation list: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#annotation.
    def visitAnnotation(self, ctx: stOTTRParser.AnnotationContext):
        print(f"Visited annotation: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#baseTemplate.
    def visitBaseTemplate(self, ctx: stOTTRParser.BaseTemplateContext):
        # print(f"Visited base template : {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#template.
    def visitTemplate(self, ctx: stOTTRParser.TemplateContext):
        print(f"Visited template: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#patternList.
    def visitPatternList(self, ctx: stOTTRParser.PatternListContext):
        print(f"Visited pattern list: {ctx.getText()}")
        result = self.visitChildren(ctx)
        print(result)
        return Patterns(result)

    # Visit a parse tree produced by stOTTRParser#instance.
    def visitInstance(self, ctx: stOTTRParser.InstanceContext):
        print(f"Visited instance: {ctx.getText()}")
        return Instance(self.visit(ctx.templateName()))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#argumentList.
    def visitArgumentList(self, ctx: stOTTRParser.ArgumentListContext):
        print(f"Visited argument list: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#argument.
    def visitArgument(self, ctx: stOTTRParser.ArgumentContext):
        print(f"Visited argument: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#type.
    def visitType(self, ctx: stOTTRParser.TypeContext):
        print(f"Visited type: {ctx.getText()}")
        return self.visitChildren(ctx)

    def visitListType(self, ctx: stOTTRParser.ListTypeContext):
        return TypedList(self.visit(ctx.type_()))

    # Visit a parse tree produced by stOTTRParser#neListType.
    def visitNeListType(self, ctx: stOTTRParser.NeListTypeContext):
        print(f"Visited NeListType: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#lubType.
    def visitLubType(self, ctx: stOTTRParser.LubTypeContext):
        print(f"Visited LubType: {ctx.getText()}")
        return self.visitChildren(ctx)

    def visitBasicType(self, ctx: stOTTRParser.BasicTypeContext):
        return Basic(ctx.getText())

    # Visit a parse tree produced by stOTTRParser#term.
    def visitTerm(self, ctx: stOTTRParser.TermContext):
        print(f"Visited term {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#constantTerm.
    def visitConstantTerm(self, ctx: stOTTRParser.ConstantTermContext):
        print(f"Visited constant term: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#constant.
    def visitConstant(self, ctx: stOTTRParser.ConstantContext):
        print(f"Visited constant: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#none.
    def visitNone(self, ctx: stOTTRParser.NoneContext):
        print(f"Visited none: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#termList.
    def visitTermList(self, ctx: stOTTRParser.TermListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#constantList.
    def visitConstantList(self, ctx: stOTTRParser.ConstantListContext):
        print(f"Visited constant list: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#turtleDoc.
    def visitTurtleDoc(self, ctx: stOTTRParser.TurtleDocContext):
        print(f"Visited turtle doc: {ctx.getText()}")
        return self.visitChildren(ctx)

    def visitDirective(self, ctx: stOTTRParser.DirectiveContext):
        return self.visitChildren(ctx)

    def visitPrefixID(self, ctx: stOTTRParser.PrefixIDContext):
        return Prefix(ctx.PNAME_NS(), ctx.IRIREF())

    # Visit a parse tree produced by stOTTRParser#base.
    def visitBase(self, ctx: stOTTRParser.BaseContext):
        print(f"Visited base: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#sparqlBase.
    def visitSparqlBase(self, ctx: stOTTRParser.SparqlBaseContext):
        print(f"Visited SPARQL base: {ctx.getText()}")
        return self.visitChildren(ctx)

    def visitSparqlPrefix(self, ctx: stOTTRParser.SparqlPrefixContext):
        return Prefix(ctx.PNAME_NS(), ctx.IRIREF())

    def visitLiteral(self, ctx: stOTTRParser.LiteralContext):
        return ctx.getText()

    def visitNumericLiteral(self, ctx: stOTTRParser.NumericLiteralContext):
        number = ctx.getText()
        if number.isdigit():
            return int(number)
        else:
            return float(number)

    # Visit a parse tree produced by stOTTRParser#rdfLiteral.
    def visitRdfLiteral(self, ctx: stOTTRParser.RdfLiteralContext):
        print(f"Visited rdf literal: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#iri.
    def visitIri(self, ctx: stOTTRParser.IriContext):
        return Iri(ctx.getText())

    # Visit a parse tree produced by stOTTRParser#prefixedName.
    def visitPrefixedName(self, ctx: stOTTRParser.PrefixedNameContext):
        print(f"Visited prefixed name: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#blankNode.
    def visitBlankNode(self, ctx: stOTTRParser.BlankNodeContext):
        print(f"Visited blank node: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by stOTTRParser#anon.
    def visitAnon(self, ctx: stOTTRParser.AnonContext):
        print(f"Visited anon: {ctx.getText()}")
        return self.visitChildren(ctx)

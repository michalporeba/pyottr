from .grammar.stOTTRParser import stOTTRParser
from .grammar.stOTTRVisitor import stOTTRVisitor as BaseVisitor
from .model import Template

class stOTTRVisitor(BaseVisitor):
    def __init__(self):
        self.templates = {}

    def visitStOTTRDoc(self, ctx:stOTTRParser.StOTTRDocContext):
        self.visitChildren(ctx)
        return { 'templates': self.templates }

    def visitStatement(self, ctx):
        print(f"Visited statement: {ctx.getText()}")
        return super().visitStatement(ctx)

    def visitSignature(self, ctx:stOTTRParser.SignatureContext):
        print(f"Visited signature: {ctx.getText()}")
        return self.visitChildren(ctx)

    def visitTemplateName(self, ctx:stOTTRParser.TemplateNameContext):
        print(f"Visited template name: {ctx.getText()}")
        self.templates[ctx.getText()] = Template(ctx.getText())
        return self.visitChildren(ctx)
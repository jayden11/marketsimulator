package generator.python

import predef._
import predef.ImportFrom
import scala.Some

object intrinsic_function extends gen.PythonGenerator
{
    import base.{Def, Prop}

    case class Parameter(p : Typed.Parameter) extends base.Parameter
    {
//        override def setter =
//            super.setter | "context.reset(self)" ||| ImportFrom("context", "marketsim")
    }

    abstract class Common(val args : List[String], val f : Typed.Function)
            extends base.Printer
            with    base.DocString
            with    base.Alias
            with    base.DecoratedName
            with    base.IntrinsicEx
            with    base.IntrinsicBaseClass
    {
        override def repr = if (label_tmpl.toString != "N/A") super.repr else ""

        override def call_body = ""  // TODO: remove from the base class
    }

    trait BaseClass_Intrinsic extends Common
    {
        override def init_body = super.init_body | s"$implementation_class.__init__(self)"

        def implementationBase = TypesBound.ImplementationClass(implementation_class, implementation_module)

        def bindImpl = Def("bind_impl", "ctx", implementation_class + ".bind_impl(self, ctx)")
        def reset = Def("reset", "", implementation_class + ".reset(self)")

        override def body = super.body | bindImpl | reset

        override def base_class_list = implementationBase :: (if (super.base_class_list != List(TypesBound.Any_)) super.base_class_list else Nil)
    }


    class Import(args : List[String], f : Typed.Function)
            extends Common(args, f)
            with    base.BaseClass_Function
            with    BaseClass_Intrinsic
    {
        override type Parameter = intrinsic_function.Parameter
        def mkParam(p : Typed.Parameter) = intrinsic_function.Parameter(p)
    }


    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        if (f.ret_type canCastTo Typed.topLevel.floatFunc)
            new Import(args, f)
        else
            new Import(args, f)
    }

    val name = "python.intrinsic.function"
}

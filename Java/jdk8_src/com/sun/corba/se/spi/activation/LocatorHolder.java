package com.sun.corba.se.spi.activation;

/**
* com/sun/corba/se/spi/activation/LocatorHolder.java .
* Generated by the IDL-to-Java compiler (portable), version "3.2"
* from /Users/java_re/workspace/8-2-build-macosx-x86_64/jdk8u221/13320/corba/src/share/classes/com/sun/corba/se/spi/activation/activation.idl
* Thursday, July 4, 2019 4:38:18 AM PDT
*/

public final class LocatorHolder implements org.omg.CORBA.portable.Streamable
{
  public com.sun.corba.se.spi.activation.Locator value = null;

  public LocatorHolder ()
  {
  }

  public LocatorHolder (com.sun.corba.se.spi.activation.Locator initialValue)
  {
    value = initialValue;
  }

  public void _read (org.omg.CORBA.portable.InputStream i)
  {
    value = com.sun.corba.se.spi.activation.LocatorHelper.read (i);
  }

  public void _write (org.omg.CORBA.portable.OutputStream o)
  {
    com.sun.corba.se.spi.activation.LocatorHelper.write (o, value);
  }

  public org.omg.CORBA.TypeCode _type ()
  {
    return com.sun.corba.se.spi.activation.LocatorHelper.type ();
  }

}

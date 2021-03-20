Sub createUniqueList():
    '#1create unique ticker list
     Dim d As Object, c As Variant, i As Long, lastrow As Long
     Set d = CreateObject("Scripting.Dictionary")
     lastrow = Cells(Rows.Count, 1).End(xlUp).Row
     c = Range("A2:A" & lastrow)
     For i = 1 To UBound(c, 1)
         d(c(i, 1)) = 1
     Next i
     Range("J2").Resize(d.Count) = Application.Transpose(d.keys)
End Sub
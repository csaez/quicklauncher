from wishlib.si import si, sisel
if sisel.Count:
    operator = si.ApplyGenOp("CrvFit", "", sisel(0))(0)
    operator.Parameters("cont").Value = 1
    si.InspectObj(operator)

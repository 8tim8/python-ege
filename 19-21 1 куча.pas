type
  arr = array[1..3] of int64;
  arr2 = array[1..300] of int64;
  
var
  s, k, l, n, i, size: int64;
  m: arr;
  pos: arr2;

procedure move(x: int64; var a: arr);
begin
  a[1] := x + 1;
  //a[2] := x + 2;
  a[2] := x * 2;
end;

function win(x: int64): boolean;
begin
  win := false;
  if x >= 106 then
    win := true;
end;

begin
  size := 106;
  for s := 1 to size do
    begin
      move(s, m);
      k := m[1];
      l := m[2];
      //n := m[3];
      if (win(k)) or (win(l)) then
        pos[s] := 1;
    end;
  for s := 1 to size do
    begin
      move(s, m);
      k := m[1];
      l := m[2];
      //n := m[3];
      if (pos[s] = 0) and ((pos[k] = 1) or (pos[l] = 1)) then
        pos[s] := -1;
    end;
  for s := 1 to size do
    begin
      move(s, m);
      k := m[1];
      l := m[2];
      //n := m[3];
      if (pos[s] = 0) and ((pos[k] = -1) or (pos[l] = -1)) then
        pos[s] := 2;
    end;
  for s := 1 to size do
    begin
      move(s, m);
      k := m[1];
      l := m[2];
      //n := m[3];
      if (pos[s] = 0) and ((pos[k] > 0) and (pos[l] > 0)) then
        pos[s] := -2;
    end;
  for s := 1 to size do
    begin
      move(s, m);
      k := m[1];
      l := m[2];
      //n := m[3];
      if (pos[s] = 0) and ((pos[k] < 0) or (pos[l] < 0)) then
        pos[s] := 3;
    end;
  for s := 1 to size do
    begin
      move(s, m);
      k := m[1];
      l := m[2];
      //n := m[3];
      if (pos[s] = 0) and ((pos[k] > 0) and (pos[l] > 0)) then
        pos[s] := -3;
    end;
  for s := 1 to size do
    begin
      move(s, m);
      k := m[1];
      l := m[2];
      //n := m[3];
      if (pos[s] = 0) and ((pos[k] < 0) or (pos[l] < 0)) then
        pos[s] := 4;
    end;
  for s := 1 to size do
    begin
      move(s, m);
      k := m[1];
      l := m[2];
      //n := m[3];
      if (pos[s] = 0) and ((pos[k] > 0) and (pos[l] > 0)) then
        pos[s] := -4;
    end;
  for i := 1 to size+1 do
    writeln(i, ' ', pos[i]);
end.
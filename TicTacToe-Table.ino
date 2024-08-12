String grid = "000000000ss";
bool PlayerOneWin = false;
bool PlayerTwoWin = false;
bool turn=false;
int polja[9] = { 4, 3, 2, 7, 6, 5, 10, 9, 8 };
bool isGood[9] = { 0, 0, 0, 0, 0, 0, 0, 0, 0 };

void setPolja() {
  for (int i = 0; i < 9; i++) {
    if (bool(digitalRead(polja[i])) && !isGood[i]) {
      grid[i] = (!turn ? '1' : '2');
      isGood[i] = 1;
      turn = !turn;
    }
  }
}
bool prazanString() {
  for(int i=0;i<9;i++)if(grid[i]=='0')return false;
  return true;
}
void setup() {
  for (int i = 2; i < 10; i++) pinMode(i, INPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
}
void loop() {
  setPolja();
  PlayerOneWin = 0;
  PlayerTwoWin = 0;
  grid[9] = 's';
  grid[10] = 's';
  //bruteforce of tic tac toe for players
  PlayerOneWin |= (grid.substring(0, 3) == "111" || grid.substring(3, 6) == "111" || grid.substring(6, 9) == "111" || (grid[0] == '1' && grid[3] == '1' && grid[6] == '1') || (grid[1] == '1' && grid[4] == '1' && grid[7] == '1') || (grid[2] == '1' && grid[5] == '1' && grid[8] == '1') || (grid[0] == '1' && grid[4] == '1' && grid[8] == '1') || (grid[2] == '1' && grid[4] == '1' && grid[6] == '1'));
  PlayerTwoWin |= (grid.substring(0, 3) == "222" || grid.substring(3, 6) == "222" || grid.substring(6, 9) == "222" || (grid[0] == '2' && grid[3] == '2' && grid[6] == '2') || (grid[1] == '2' && grid[4] == '2' && grid[7] == '2') || (grid[2] == '2' && grid[5] == '2' && grid[8] == '2') || (grid[0] == '2' && grid[4] == '2' && grid[8] == '2') || (grid[2] == '2' && grid[4] == '2' && grid[6] == '2'));
  if (!prazanString()) {
    if (PlayerOneWin) {
      grid[9] = 'p';
      grid[10] = '1';
    }
    if (PlayerTwoWin) {
      grid[9] = 'p';
      grid[10] = '2';
    }
  } else {
    if (PlayerOneWin) {
      grid[9] = 'p';
      grid[10] = '1';
    } else if (PlayerTwoWin) {
      grid[9] = 'p';
      grid[10] = '2';
    } else {
      grid[9] = 'd';
      grid[10] = 'r';
    }
  }
  Serial.println(grid);
  delay(100);
}
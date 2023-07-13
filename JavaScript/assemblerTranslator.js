const infijoAPosfijo = (exp) => {
  // Mapa de precedencia de operadores
  let precedencia = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
  };

  let resultado = [];
  let operadores = [];

  // Separa la expresión en tokens (números y operadores)
  let tokens = exp.split(/\s+/);
  
  // Itera sobre los tokens
  for (let i = 0; i < tokens.length; i++) {
    let token = tokens[i];

    // Si el token es un número, lo añade al resultado
    if (!isNaN(token)) {
      resultado.push(token);
    }

    // Si el token es un operador
    else if (token in precedencia) {
      // Mientras haya operadores en la pila y el operador actual tenga menor o igual precedencia
      while (operadores.length > 0 && operadores[operadores.length - 1] != "(" && precedencia[token] <= precedencia[operadores[operadores.length - 1]]) {
        // Añade el operador de la pila al resultado
        resultado.push(operadores.pop());
      }

      // Añade el operador actual a la pila
      operadores.push(token);
    }

    // Si el token es un paréntesis izquierdo
    else if (token == "(") {
      operadores.push(token);
    }

    // Si el token es un paréntesis derecho
    else if (token == ")") {
      // Mientras el último operador en la pila no sea un paréntesis izquierdo
      while (operadores.length > 0 && operadores[operadores.length - 1] != "(") {
        // Añade el operador de la pila al resultado
        resultado.push(operadores.pop());
      }

      // Si la pila está vacía o el último operador en la pila es un paréntesis izquierdo, elimina el paréntesis izquierdo de la           pila
      if (operadores.length == 0 || operadores[operadores.length - 1] == "(") {
        operadores.pop();
      }
    }
  }

  // Añade los operadores restantes en la pila al resultado
  while (operadores.length > 0) {
    resultado.push(operadores.pop());
  }

  // Une los tokens del resultado en una cadena
  let resultadoString = resultado.join("");
  return resultadoString;
}

// --------------------------------------------------

const codetoAssembler = (op) => {
  // Hacemos una tabla de simbolos
  let table = {
    '+': 'ADD',
    '-': 'SUB',
    '*': 'MUL',
    '/': 'DIV',
  };
  
  let registers = {
    '1': 'R0',
    '2': 'R1',
    '3': 'R2',
    '4': 'R3',
    '5': 'R4',
    '6': 'R5',
    '7': 'R6',
    '8': 'R7',
    '9': 'R8',
    '10': 'R9',
  };
  
  let result = "\n";
  const exp = infijoAPosfijo(op);
  let tokens = exp.split('');
  for (let i = 0; i < tokens.length; i++) {
    let token = tokens[i];
    // Si el token es un número, lo añade al resultado
    if (!isNaN(parseFloat(token))) {
      result += "MOV " + token + ',' + registers[i+1] + '\n';
    }
    // Si el token es un operador, lo traduce y añade al resultado
    if(token in table){
      result += table[token] + ' ' + registers[i-1] + ',' + registers[i] + '\n';
    }
    // Si el token es una letra, lo mueve a memoria
    if(isNaN(parseFloat(token)) && !(token in table)){
      result += "MOV" + token + registers[i];
    }
  };
  console.log(result);
}

codetoAssembler("3 + 4 * 2 / ( 1 - 5 )");
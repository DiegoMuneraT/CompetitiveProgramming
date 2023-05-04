const infijoAPosfijo = (exp) => {
  // Mapa de precedencia de operadores
  let precedencia = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3
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
    '*': 'MULT',
    '/': 'DIV',
    '^': 'POT',
  };
  let result = "\n";
  const exp = infijoAPosfijo(op);
  let tokens = exp.split('');
  
  for (let i = 0; i < tokens.length; i++) {
    let token = tokens[i];
    // Si el token es un número, lo añade al resultado
    if (!isNaN(token)) {
      result += token + '\n';
    // Si el token es un operador, lo traduce y añade al resultado
    } else if(token in table){
      result += table[token] + '\n'
    }
  };
  console.log(result)  
}

// --------------------------------------------------
// Ejecución del programa:
//  -Es una calculadora simple que puede traducir operaciones aritmeticas simples o conjuntas de: +,-,*,/,^ a lenguaje    ensamblador.
//  -La única condicion es separar por espacios en blanco cada caracter
//  -La entrada debe ser un String por ejemplo 5+1 es una entrada incorrecta, debe ser "5+1"
codetoAssembler("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3")
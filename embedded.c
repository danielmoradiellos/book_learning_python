#include <Python.h>

int main(void){
Py_Initialize();
PyRun_SimpleString("x = 'brave ' + 'sir robin'");
PyRun_SimpleString("print x");

return 0;
}

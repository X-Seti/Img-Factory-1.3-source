#include "CDebugger.h"
#include "CFileUtility.h"

using namespace std;

void		CDebugger::log(string strData)
{
	std::string strPath = "C:\\Users\\James\\Desktop\\DEBUG FILE.txt";
	CFileUtility::storeFile(strPath, strData + "\r\n", true, true);
}
#include "CCOLFile.h"
#include "CCOLEntry.h"

using namespace std;

vector<string>		CCOLFile::getModelNames(void)
{
	vector<string> vecModelNames;
	for (auto pCOLEntry : m_vecEntries)
	{
		vecModelNames.push_back(pCOLEntry->m_strModelName);
	}
	return vecModelNames;
}
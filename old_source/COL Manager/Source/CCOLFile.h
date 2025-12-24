#ifndef CCOLFile_H
#define CCOLFile_H

#include <string>
#include <vector>

struct CCOLEntry;

struct CCOLFile
{
	std::vector<std::string>		getModelNames(void);

	std::string						m_strFilePath;
	std::vector<CCOLEntry*>			m_vecEntries;
};

#endif
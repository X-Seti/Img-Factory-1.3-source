#ifndef CIDEManager_H
#define CIDEManager_H

#include "eIDEFileSection.h"
#include <string>
#include <vector>

struct CIDEFile;
class CIDESectionEntry;

class CIDEManager
{
public:
	static CIDEManager*	getInstance(void);

	CIDEFile*			parseFile(std::string strPath);
	void				storeFile(CIDEFile *pIDEFile);

private:
	eIDEFileSection		getIDESectionFromString(std::string strType);
	void				addCommentLinesToEntry(CIDESectionEntry *pEntry, std::vector<std::string>& vecPreviousCommentLines);
	void				writePreviousCommentLines(CIDESectionEntry *pEntry);

	static CIDEManager*	m_pInstance;
};

#endif
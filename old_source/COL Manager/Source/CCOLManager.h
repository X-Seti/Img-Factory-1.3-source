#ifndef CCOLManager_H
#define CCOLManager_H

#include <string>

struct CCOLFile;

class CCOLManager
{
public:
	static CCOLManager*	getInstance(void);

	CCOLFile*			parseFile(std::string strPath);
	void				storeFile(CCOLFile *pCOLFile);

private:
	static CCOLManager*	m_pInstance;
};

#endif
#ifndef CPathUtility_H
#define CPathUtility_H

#include <string>

class CPathUtility
{
public:
	static std::string			getFileName(std::string strPath);
	static std::string			getFileExtension(std::string strPath);
	static std::string			replaceExtension(std::string strPath, std::string strExtension);
	static std::string			removeExtension(std::string strPath);
	static std::string			addSlashToEnd(std::string strPath);
};

#endif
#ifndef CRegistryUtility_H
#define CRegistryUtility_H

#include <string>

class CRegistryUtility
{
public:
	static void				setRegistryValueString(std::string strKey1, std::string strKey2, std::string strValue);
	static std::string		getRegistryValueString(std::string strKey1, std::string strKey2);
	static void				setRegistryValueInt(std::string strKey1, std::string strKey2, int iValue);
	static int				getRegistryValueInt(std::string strKey1, std::string strKey2);
	
};

#endif
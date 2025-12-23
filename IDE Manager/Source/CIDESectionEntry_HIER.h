#ifndef CIDESectionEntry_HIER_H
#define CIDESectionEntry_HIER_H

#include "CIDESectionEntry.h"
#include <string>

struct CIDESectionEntry_HIER : public CIDESectionEntry
{
	unsigned long				m_uiObjectId;
	std::string					m_strModelName;
	std::string					m_strTextureName;
};

#endif
#ifndef CIDESectionEntry_TXDP_H
#define CIDESectionEntry_TXDP_H

#include "CIDESectionEntry.h"
#include <string>

struct CIDESectionEntry_TXDP : public CIDESectionEntry
{
	std::string					m_strTextureName;
	std::string					m_strTextureParentName;
};

#endif
#ifndef CIDESectionEntry_PEDS_H
#define CIDESectionEntry_PEDS_H

#include "CIDESectionEntry.h"
#include <string>

struct CIDESectionEntry_PEDS : public CIDESectionEntry
{
	unsigned long				m_uiObjectId;
	std::string					m_strModelName;
	std::string					m_strTextureName;
	std::string					m_strDefaultPedType;
	std::string					m_strBehaviour;
	std::string					m_strAnimationGroup;
	unsigned long				m_uiCarsCanDrive;
	std::string					m_strAnimationFile;
	unsigned long				m_uiPreferredRadioStations[2];
	std::string					m_strVoiceArchive;
	std::string					m_strVoices[2];
};

#endif
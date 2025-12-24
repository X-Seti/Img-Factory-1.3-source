#include "CIDEFile.h"
#include "CIDESectionEntry_OBJS.h"
#include "CIDESectionEntry_TOBJ.h"
#include "CIDESectionEntry_ANIM.h"
#include "CIDESectionEntry_PEDS.h"
#include "CIDESectionEntry_WEAP.h"
#include "CIDESectionEntry_CARS.h"
#include "CIDESectionEntry_HIER.h"
#include "CIDESectionEntry_TXDP.h"
#include "CIDESectionEntry_2DFX_Lights.h"
#include "CIDESectionEntry_2DFX_Particles.h"
#include "CIDESectionEntry_2DFX_Unknown1.h"
#include "CIDESectionEntry_2DFX_Peds.h"
#include "CIDESectionEntry_2DFX_SunReflections.h"
#include "CIDESectionEntry_PATH.h"
#include "CIDESectionEntry_HAND.h"

using namespace std;

vector<string>		CIDEFile::getModelNames(void)
{
	vector<string> vecModelNames;
	for (auto pEntry : m_vecSectionEntries_OBJS) vecModelNames.push_back(pEntry->m_strModelName);
	for (auto pEntry : m_vecSectionEntries_TOBJ) vecModelNames.push_back(pEntry->m_strModelName);
	for (auto pEntry : m_vecSectionEntries_ANIM) vecModelNames.push_back(pEntry->m_strModelName);
	for (auto pEntry : m_vecSectionEntries_PEDS) vecModelNames.push_back(pEntry->m_strModelName);
	for (auto pEntry : m_vecSectionEntries_WEAP) vecModelNames.push_back(pEntry->m_strModelName);
	for (auto pEntry : m_vecSectionEntries_CARS) vecModelNames.push_back(pEntry->m_strModelName);
	for (auto pEntry : m_vecSectionEntries_HIER) vecModelNames.push_back(pEntry->m_strModelName);
	//for (auto pEntry : m_vecSectionEntries_TXDP) vecModelNames.push_back(pEntry->m_strModelName);
	//for (auto pEntry : m_vecSectionEntries_2DFX_Lights) vecModelNames.push_back(pEntry->m_strModelName);
	//for (auto pEntry : m_vecSectionEntries_2DFX_Particles) vecModelNames.push_back(pEntry->m_strModelName);
	//for (auto pEntry : m_vecSectionEntries_2DFX_Unknown1) vecModelNames.push_back(pEntry->m_strModelName);
	//for (auto pEntry : m_vecSectionEntries_2DFX_Peds) vecModelNames.push_back(pEntry->m_strModelName);
	//for (auto pEntry : m_vecSectionEntries_2DFX_SunReflections) vecModelNames.push_back(pEntry->m_strModelName);
	//for (auto pEntry : m_vecSectionEntries_PATH) vecModelNames.push_back(pEntry->m_strModelName);
	//for (auto pEntry : m_vecSectionEntries_HAND) vecModelNames.push_back(pEntry->m_strModelName);
	return vecModelNames;
}
vector<string>		CIDEFile::getTextureNames(void)
{
	vector<string> vecModelNames;
	for (auto pEntry : m_vecSectionEntries_OBJS) vecModelNames.push_back(pEntry->m_strTextureName);
	for (auto pEntry : m_vecSectionEntries_TOBJ) vecModelNames.push_back(pEntry->m_strTextureName);
	for (auto pEntry : m_vecSectionEntries_ANIM) vecModelNames.push_back(pEntry->m_strTextureName);
	for (auto pEntry : m_vecSectionEntries_PEDS) vecModelNames.push_back(pEntry->m_strTextureName);
	for (auto pEntry : m_vecSectionEntries_WEAP) vecModelNames.push_back(pEntry->m_strTextureName);
	for (auto pEntry : m_vecSectionEntries_CARS) vecModelNames.push_back(pEntry->m_strTextureName);
	for (auto pEntry : m_vecSectionEntries_HIER) vecModelNames.push_back(pEntry->m_strTextureName);
	for (auto pEntry : m_vecSectionEntries_TXDP) vecModelNames.push_back(pEntry->m_strTextureName);
	//for (auto pEntry : m_vecSectionEntries_2DFX_Lights) vecModelNames.push_back(pEntry->m_strTextureName);
	//for (auto pEntry : m_vecSectionEntries_2DFX_Particles) vecModelNames.push_back(pEntry->m_strTextureName);
	//for (auto pEntry : m_vecSectionEntries_2DFX_Unknown1) vecModelNames.push_back(pEntry->m_strTextureName);
	//for (auto pEntry : m_vecSectionEntries_2DFX_Peds) vecModelNames.push_back(pEntry->m_strTextureName);
	//for (auto pEntry : m_vecSectionEntries_2DFX_SunReflections) vecModelNames.push_back(pEntry->m_strTextureName);
	//for (auto pEntry : m_vecSectionEntries_PATH) vecModelNames.push_back(pEntry->m_strTextureName);
	//for (auto pEntry : m_vecSectionEntries_HAND) vecModelNames.push_back(pEntry->m_strTextureName);
	return vecModelNames;
}
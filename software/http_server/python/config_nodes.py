# -*- coding: utf-8 -*-

MAC = 'strMac'
NAME = 'strName'
LAB_NAME = 'strLabName'
RESPONSIBLE = 'strResposible'
GIT_TAGS = 'strGitTags'
USER_TAG = 'strUserTag'
NODES = 'listNodes'

dictNodes = {}
dictLabs = {}

dictNodes['20180907_01'] = {
  MAC: '3C71BF0F97A4',
  NAME: 'steel',
}

dictNodes['20180907_03'] = {
  MAC: '840D8E1BC40C',
  NAME: 'aluminium',
}

dictLabs['labHombi'] = {
  LAB_NAME: 'hombrechtikon',
  RESPONSIBLE: 'Peter Maerki',
  GIT_TAGS: 'x1.0;y1.1',
  USER_TAG: '1',
  NODES: (
    '20180907_01',
  )
}

dictLabs['labY'] = {
  LAB_NAME: 'ETH, LabY',
  RESPONSIBLE: 'Robin',
  GIT_TAGS: 'y1.1;x1.0',
  USER_TAG: '1',
  NODES: (
    '20180907_03',
  )
}

if __name__ == '__main__':
  # Test if the configuration may collect all files from github.
  import python3_github_pull
  for strLab, dictLab in dictLabs.items():
    try:
      p = python3_github_pull.GithubPull(strDirectory='.', strGitTags=dictLab[GIT_TAGS], strUserTag=dictLab[USER_TAG])
      strTarFilenameFull = p.getTar()
      print('Lab "%s": %s' % (strLab, strTarFilenameFull))
    except Exception:
      print('ERROR in Lab "%s"' % strLab)
      raise


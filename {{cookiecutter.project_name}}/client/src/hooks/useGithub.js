import path from 'path'
import { useQuery } from 'react-query'

// Utils
import fs from 'fs'
import iniParser from '../utils/iniparser'

const parseConfig = config => {
  const parsedConfig = config

  return parsedConfig
}

const findConfig = async (filePath, filter, callback) => {
  // TODO add cancel search

  try {
    if (!fs.existsSync(filePath)) {
      console.log('no dir ', filePath)
    }

    const files = fs.readdirSync(filePath)
    const fileName = files.find(file => file === '.gitconfig')

    if (fileName) {
      const gitConfig = await iniParser(path.join(filePath, fileName))
      return gitConfig
    }

    // files.forEach((file) => {
    //   // console.log('file:', file)

    //   if (file === '.gitconfig') {
    //     const filename = path.join(filePath, file)
    //     const stat = fs.lstatSync(filename)

    //     if (stat.isDirectory()) {
    //       findConfig(filename, filter) // recurse
    //     } else if (filename.indexOf(filter) >= 0) {
    //       console.log('-- found: ', filename)
    //     }
    //   }
    // })
  } catch (error) {
    console.error(error)
  }

  return null
}

const getGitHub = async () => {
  const config = await findConfig('/Users/sean.baier/', '.gitconfig')

  let parsedConfigFile
  if (config) {
    parsedConfigFile = parseConfig(config)
  }

  return parsedConfigFile
}

export default function useGithub() {
  return useQuery('github', getGitHub)
}
